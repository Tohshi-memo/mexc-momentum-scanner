# Decision Report

- generated_at: 2026-11-26T01:16:46.026920+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19661**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19661, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.27% | **-1.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.30% | **+0.22%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.65% | **-0.29%** |
| LIMIT_ATR | 16/20 | 80.0% | -0.55% | **-0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +4.14% | **+1.24%** |
| LIMIT_6PCT_LONG | 5/20 | 25.0% | +3.57% | **+0.89%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.39% | **+0.84%** |
| MARKET_LONG | 20/20 | 100.0% | +0.77% | **+0.77%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.02% | **+0.77%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 289件 (TP 105 / SL 176 / EXP 8)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,978.37** / 初期 $100.00 (+1878.37%)
- 確定: 7613件 (Win 2191 / Loss 2451 / Flat 2971) / skip 8609件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,978.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$465.65** / 初期 $100.00 (+365.65%)
- 確定: 5221件 (Win 1389 / Loss 1125 / Flat 2707) / skip 7851件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $465.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7824件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000195 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-26T01:16:28.843211+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.48% price=60786.6
- Funnel: target 1097 → liquid 155 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +37.40% | $1,397,879.15 |
| MANTRA/USDT:USDT | +35.88% | $4,143,493.90 |
| SOXL/USDT:USDT | +30.74% | $1,898,461,043.04 |
| AKE/USDT:USDT | +27.76% | $5,960,419.83 |
| SNXX/USDT:USDT | +25.46% | $33,923,148.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MVLL/USDT:USDT | below_1h_threshold | +3.70% | +3.22% |
| RAM/USDT:USDT | below_1h_threshold | +3.43% | +2.95% |
| SOXL/USDT:USDT | below_1h_threshold | +3.18% | +2.70% |
| MUU/USDT:USDT | below_1h_threshold | +3.14% | +2.66% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +2.94% | +2.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
