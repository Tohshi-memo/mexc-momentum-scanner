# Decision Report

- generated_at: 2026-11-02T20:46:13.589827+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18033**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18033, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.10% | **+0.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.30% | **+0.81%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.95% | **+0.67%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.84% | **+0.63%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.68% | **+1.51%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.59% | **+1.19%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.07% | **+1.14%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.25% | **+1.13%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.12% | **+0.95%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 258件 (TP 95 / SL 155 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,550.82** / 初期 $100.00 (+1450.82%)
- 確定: 6885件 (Win 1997 / Loss 2208 / Flat 2680) / skip 7709件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGT/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $1,550.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$385.53** / 初期 $100.00 (+285.53%)
- 確定: 4473件 (Win 1202 / Loss 995 / Flat 2276) / skip 6971件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0287 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGT/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $385.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6192件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000170 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-02T20:46:02.670632+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=76899.4
- Funnel: target 1093 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +17.63% | $2,017,997.42 |
| SOXS/USDT:USDT | +12.01% | $20,412,772.52 |
| SQQQ/USDT:USDT | +6.26% | $1,493,642.96 |
| JCT/USDT:USDT | +5.04% | $2,084,087.44 |
| HOT/USDT:USDT | +4.94% | $3,688,401.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOT/USDT:USDT | below_1h_threshold | +2.32% | +2.54% |
| LYN/USDT:USDT | below_1h_threshold | +1.88% | +2.09% |
| SOXS/USDT:USDT | below_1h_threshold | +1.72% | +1.94% |
| SQQQ/USDT:USDT | below_1h_threshold | +1.28% | +1.50% |
| XMR/USDT:USDT | below_1h_threshold | +1.08% | +1.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
