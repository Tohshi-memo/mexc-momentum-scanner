# Decision Report

- generated_at: 2026-07-01T22:22:50.641556+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8023**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=8023, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.83% | **+0.83%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_10PCT | 5/20 | 25.0% | +2.69% | **+0.67%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +5.02% | **+0.50%** |
| LIMIT_9PCT | 5/20 | 25.0% | +1.83% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.40% | **+2.40%** |
| ASK_LONG | 20/20 | 100.0% | +1.78% | **+1.78%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.72% | **+0.51%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.67% | **+0.13%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.25% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.80** / 初期 $100.00 (+184.80%)
- 確定: 2420件 (Win 744 / Loss 802 / Flat 874) / skip 2164件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAIKO/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $284.80

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.46** / 初期 $100.00 (+6.46%)
- 確定: 538件 (Win 135 / Loss 127 / Flat 276) / skip 896件
- 成長率目線: 平均log +0.000116 / 幾何平均 +0.012% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAIKO/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $106.46

## 5. Latest Market Context

- 更新: 2026-07-01T22:22:44.431155+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.30% price=60982.8
- Funnel: target 825 → liquid 157 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.4 >= 65=1, 4h RSI 91.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAIKO/USDT:USDT | +81.03% | $26,139,545.80 |
| TLM/USDT:USDT | +73.31% | $3,853,497.86 |
| NOM/USDT:USDT | +24.45% | $5,488,607.87 |
| LIT/USDT:USDT | +20.53% | $8,635,201.43 |
| COOKIE/USDT:USDT | +17.18% | $1,044,088.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +2.90% | +2.60% |
| BTW/USDT:USDT | below_1h_threshold | +2.74% | +2.43% |
| O/USDT:USDT | below_1h_threshold | +2.08% | +1.77% |
| VELVET/USDT:USDT | below_1h_threshold | +2.01% | +1.71% |
| NOM/USDT:USDT | below_1h_threshold | +1.86% | +1.55% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
