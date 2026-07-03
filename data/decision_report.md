# Decision Report

- generated_at: 2026-07-03T15:12:15.699751+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8166**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.50% / filled 20/20。**
- 全期間 MARKET基準: n=8166, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.50% | **+2.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.50% | **+2.50%** |
| ASK | 20/20 | 100.0% | +2.43% | **+2.43%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.02% | **+1.62%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.18% | **+0.77%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.67% | **+0.37%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.21% | **+0.12%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.13% | **+0.08%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.50% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$102.61** / 初期 $100.00 (+2.61%)
- 確定トレード: 56件 (TP 20 / SL 35 / EXP 1)
- 最新: RIF/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$286.01** / 初期 $100.00 (+186.01%)
- 確定: 2487件 (Win 764 / Loss 831 / Flat 892) / skip 2240件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RIF/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $286.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.04** / 初期 $100.00 (+6.04%)
- 確定: 611件 (Win 147 / Loss 147 / Flat 317) / skip 966件
- 成長率目線: 平均log +0.000096 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BAS/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $106.04

## 5. Latest Market Context

- 更新: 2026-07-03T15:12:10.573516+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=62299.6
- Funnel: target 834 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| THE/USDT:USDT | +48.68% | $4,367,706.05 |
| NEX/USDT:USDT | +41.64% | $3,286,995.76 |
| ARPA/USDT:USDT | +33.12% | $6,473,485.51 |
| RIF/USDT:USDT | +29.02% | $10,253,531.52 |
| ZKP/USDT:USDT | +28.61% | $5,993,743.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BICO/USDT:USDT | below_1h_threshold | +3.84% | +3.58% |
| POPCAT/USDT:USDT | below_1h_threshold | +1.42% | +1.17% |
| SEI/USDT:USDT | below_1h_threshold | +1.37% | +1.12% |
| ZEC/USDT:USDT | below_1h_threshold | +1.33% | +1.07% |
| ZKP/USDT:USDT | below_1h_threshold | +1.27% | +1.01% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
