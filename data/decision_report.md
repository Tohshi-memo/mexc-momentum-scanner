# Decision Report

- generated_at: 2026-07-01T08:42:28.451315+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7963**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7963, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.26% | **-0.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +2.74% | **+0.41%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.33% | **+0.27%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| ASK_LONG | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +1.15% | **+0.58%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$258.37** / 初期 $100.00 (+158.37%)
- 確定: 2362件 (Win 717 / Loss 787 / Flat 858) / skip 2162件
- 成長率目線: 平均log +0.000402 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASED/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $258.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.00** / 初期 $100.00 (+7.00%)
- 確定: 502件 (Win 128 / Loss 121 / Flat 253) / skip 872件
- 成長率目線: 平均log +0.000135 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $107.00

## 5. Latest Market Context

- 更新: 2026-07-01T08:42:23.687995+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=58617.7
- Funnel: target 820 → liquid 151 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAIKO/USDT:USDT | +26.14% | $1,602,429.94 |
| BASED/USDT:USDT | +19.64% | $9,837,946.43 |
| BTW/USDT:USDT | +17.35% | $10,003,246.34 |
| M/USDT:USDT | +13.36% | $4,389,446.90 |
| TRIA/USDT:USDT | +12.32% | $1,191,056.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +3.77% | +3.98% |
| ZBT/USDT:USDT | below_1h_threshold | +3.07% | +3.28% |
| TIA/USDT:USDT | below_1h_threshold | +2.14% | +2.35% |
| JTO/USDT:USDT | below_1h_threshold | +1.87% | +2.08% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +1.45% | +1.66% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
