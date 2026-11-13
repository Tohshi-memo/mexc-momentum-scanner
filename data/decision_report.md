# Decision Report

- generated_at: 2026-11-13T17:46:44.443099+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18855**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18855, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 12/20 | 60.0% | +1.89% | **+1.13%** |
| LIMIT_7PCT | 6/20 | 30.0% | +3.40% | **+1.02%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.45% | **+0.94%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.53% | **+0.88%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.95% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.42% | **+0.92%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.96% | **+0.88%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.40% | **+0.84%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定トレード: 275件 (TP 99 / SL 168 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,763.10** / 初期 $100.00 (+1663.10%)
- 確定: 7289件 (Win 2100 / Loss 2337 / Flat 2852) / skip 8127件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BARD/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $1,763.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$409.68** / 初期 $100.00 (+309.68%)
- 確定: 4863件 (Win 1306 / Loss 1078 / Flat 2479) / skip 7403件
- 成長率目線: 平均log +0.000290 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_8PCT` (selected_by_robust_growth_score) / robust_score +0.1688 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IDOL/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $409.68

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7019件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000449 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-13T17:46:30.181111+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.42% price=68950.0
- Funnel: target 1084 → liquid 148 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +19.15% | $53,775,147.68 |
| JCT/USDT:USDT | +12.12% | $7,506,891.67 |
| ARIA/USDT:USDT | +10.53% | $8,262,877.28 |
| H/USDT:USDT | +10.19% | $1,688,864.33 |
| INIT/USDT:USDT | +7.00% | $3,079,163.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INIT/USDT:USDT | below_relative_strength | +5.00% | +4.59% |
| H/USDT:USDT | below_1h_threshold | +3.69% | +3.28% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +3.50% | +3.09% |
| MVLL/USDT:USDT | below_1h_threshold | +2.96% | +2.54% |
| NIGHT/USDT:USDT | below_1h_threshold | +1.85% | +1.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
