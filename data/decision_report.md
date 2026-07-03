# Decision Report

- generated_at: 2026-07-03T19:37:33.484994+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8187**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.95% / filled 20/20。**
- 全期間 MARKET基準: n=8187, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.95% | **+0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.68% | **+0.55%** |
| LIMIT_8PCT | 4/20 | 20.0% | -0.15% | **-0.03%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | -0.15% | **-0.08%** |
| LIMIT_7PCT | 4/20 | 20.0% | -0.60% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.83% | **+0.83%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.55% | **+0.33%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.98% | **+0.15%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.14% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$287.62** / 初期 $100.00 (+187.62%)
- 確定: 2506件 (Win 769 / Loss 834 / Flat 903) / skip 2242件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TLM/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $287.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.04** / 初期 $100.00 (+6.04%)
- 確定: 611件 (Win 147 / Loss 147 / Flat 317) / skip 987件
- 成長率目線: 平均log +0.000096 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BAS/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $106.04

## 5. Latest Market Context

- 更新: 2026-07-03T19:37:27.002307+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=62163.6
- Funnel: target 834 → liquid 162 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TLM/USDT:USDT | +54.63% | $17,575,644.98 |
| ANSEM/USDT:USDT | +36.14% | $1,424,382.53 |
| MAGMA/USDT:USDT | +34.85% | $10,294,260.75 |
| BAS/USDT:USDT | +18.35% | $3,254,135.53 |
| TA/USDT:USDT | +13.76% | $2,108,530.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ANSEM/USDT:USDT | below_1h_threshold | +4.71% | +4.73% |
| MAGMA/USDT:USDT | below_1h_threshold | +4.26% | +4.29% |
| GPS/USDT:USDT | below_1h_threshold | +3.27% | +3.30% |
| US/USDT:USDT | below_1h_threshold | +3.26% | +3.29% |
| NOM/USDT:USDT | below_1h_threshold | +3.02% | +3.05% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
