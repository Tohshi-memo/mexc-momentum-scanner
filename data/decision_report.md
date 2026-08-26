# Decision Report

- generated_at: 2026-08-26T08:51:37.066319+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12686**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12686, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.46% | **+0.14%** |
| LIMIT_7PCT | 5/20 | 25.0% | +0.08% | **+0.02%** |
| LIMIT_8PCT | 3/20 | 15.0% | -1.43% | **-0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.67% | **+2.13%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.20% | **+1.87%** |
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.39% | **+1.31%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$700.46** / 初期 $100.00 (+600.46%)
- 確定: 4588件 (Win 1395 / Loss 1506 / Flat 1687) / skip 4659件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BMT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $700.46

## 4. Robust Adaptive DryRun ($100)

- 残高: **$158.78** / 初期 $100.00 (+58.78%)
- 確定: 1983件 (Win 540 / Loss 473 / Flat 970) / skip 4114件
- 成長率目線: 平均log +0.000233 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BMT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $158.78

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.83** / 初期 $100.00 (+16.83%)
- 確定: 1962件 (Win 577 / Loss 747 / Flat 638) / pending 6件 / skip 2194件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000504 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BMT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $116.83

## 6. Latest Market Context

- 更新: 2026-08-26T08:51:26.681951+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=78886.3
- Funnel: target 1018 → liquid 169 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.1 >= 65=1, 4h RSI 80.1 >= 65=1, 4h RSI 76.2 >= 65=1, 4h RSI 65.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +179.25% | $11,620,688.12 |
| BMT/USDT:USDT | +51.33% | $13,069,251.25 |
| TAC/USDT:USDT | +35.56% | $5,293,942.21 |
| LONGXIA/USDT:USDT | +34.23% | $1,941,651.21 |
| PONS/USDT:USDT | +20.60% | $1,132,973.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +4.86% | +4.86% |
| PROM/USDT:USDT | below_1h_threshold | +3.23% | +3.23% |
| TWT/USDT:USDT | below_1h_threshold | +1.18% | +1.19% |
| USELESS/USDT:USDT | below_1h_threshold | +1.17% | +1.17% |
| COW/USDT:USDT | below_1h_threshold | +1.17% | +1.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
