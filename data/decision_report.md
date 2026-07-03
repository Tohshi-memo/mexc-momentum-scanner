# Decision Report

- generated_at: 2026-07-03T19:56:46.426461+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8191**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8191, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.85% | **-0.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -2.06% | **-0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.45% | **+1.45%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.05% | **+0.92%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.20% | **+0.84%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.02% | **+0.77%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$286.18** / 初期 $100.00 (+186.18%)
- 確定: 2510件 (Win 770 / Loss 836 / Flat 904) / skip 2242件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TLM/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $286.18

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.04** / 初期 $100.00 (+6.04%)
- 確定: 611件 (Win 147 / Loss 147 / Flat 317) / skip 991件
- 成長率目線: 平均log +0.000096 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BAS/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $106.04

## 5. Latest Market Context

- 更新: 2026-07-03T19:56:38.022707+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=62201.8
- Funnel: target 834 → liquid 162 → pre 50 → checked 50 → surge 6 → strict 3
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.5 >= 65=1, 4h RSI 85.8 >= 65=1, 4h RSI 77.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TLM/USDT:USDT | +58.32% | $19,633,346.50 |
| ANSEM/USDT:USDT | +41.18% | $1,513,214.92 |
| MAGMA/USDT:USDT | +36.95% | $10,970,570.50 |
| BAS/USDT:USDT | +19.33% | $3,303,574.52 |
| GPS/USDT:USDT | +13.67% | $1,881,486.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASED/USDT:USDT | below_1h_threshold | +4.01% | +3.98% |
| US/USDT:USDT | below_1h_threshold | +3.91% | +3.88% |
| BEAT/USDT:USDT | below_1h_threshold | +3.45% | +3.42% |
| NEX/USDT:USDT | below_1h_threshold | +1.94% | +1.91% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +1.51% | +1.48% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
