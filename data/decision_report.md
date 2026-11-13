# Decision Report

- generated_at: 2026-11-13T17:56:26.719094+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18857**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18857, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 12/20 | 60.0% | +1.82% | **+1.09%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.84% | **+0.99%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.87% | **+0.93%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.87% | **+0.52%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.10% | **+0.38%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.83% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定トレード: 275件 (TP 99 / SL 168 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,763.10** / 初期 $100.00 (+1663.10%)
- 確定: 7289件 (Win 2100 / Loss 2337 / Flat 2852) / skip 8129件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BARD/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $1,763.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$409.68** / 初期 $100.00 (+309.68%)
- 確定: 4865件 (Win 1306 / Loss 1078 / Flat 2481) / skip 7403件
- 成長率目線: 平均log +0.000290 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_8PCT` (selected_by_robust_growth_score) / robust_score +0.1627 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $409.68

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7020件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000459 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-13T17:56:13.122168+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.40% price=68939.2
- Funnel: target 1084 → liquid 148 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +20.00% | $54,421,694.66 |
| H/USDT:USDT | +11.15% | $1,698,511.33 |
| ARIA/USDT:USDT | +10.39% | $8,276,021.85 |
| JCT/USDT:USDT | +6.04% | $7,755,822.93 |
| INIT/USDT:USDT | +5.47% | $3,109,240.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| Q/USDT:USDT | below_1h_threshold | +4.68% | +4.28% |
| JCT/USDT:USDT | below_1h_threshold | +4.35% | +3.95% |
| H/USDT:USDT | below_1h_threshold | +4.28% | +3.88% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +3.50% | +3.10% |
| INIT/USDT:USDT | below_1h_threshold | +3.10% | +2.70% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
