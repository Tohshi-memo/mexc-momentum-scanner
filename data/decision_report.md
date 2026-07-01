# Decision Report

- generated_at: 2026-07-01T21:46:05.435553+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8020**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.00% / filled 20/20。**
- 全期間 MARKET基準: n=8020, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+2.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.03% | **+2.03%** |
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.70% | **+0.55%** |
| LIMIT_7PCT | 7/20 | 35.0% | +0.63% | **+0.22%** |
| LIMIT_8PCT | 6/20 | 30.0% | +0.57% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.13% | **+0.53%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.15% | **+0.52%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.81% | **+0.16%** |
| ASK_LONG | 20/20 | 100.0% | +0.15% | **+0.15%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$277.80** / 初期 $100.00 (+177.80%)
- 確定: 2417件 (Win 741 / Loss 802 / Flat 874) / skip 2164件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAIKO/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $277.80

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.21** / 初期 $100.00 (+7.21%)
- 確定: 536件 (Win 135 / Loss 125 / Flat 276) / skip 895件
- 成長率目線: 平均log +0.000130 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAIKO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $107.21

## 5. Latest Market Context

- 更新: 2026-07-01T21:45:59.321837+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.15% price=60790.0
- Funnel: target 825 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TLM/USDT:USDT | +58.80% | $3,225,133.71 |
| TAIKO/USDT:USDT | +33.33% | $22,045,142.35 |
| NOM/USDT:USDT | +20.74% | $5,141,866.86 |
| LIT/USDT:USDT | +20.65% | $8,142,357.34 |
| RIF/USDT:USDT | +13.64% | $2,925,361.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NOM/USDT:USDT | below_relative_strength | +5.58% | +4.44% |
| PIPPIN/USDT:USDT | below_1h_threshold | +4.24% | +3.09% |
| O/USDT:USDT | below_1h_threshold | +4.23% | +3.08% |
| BTW/USDT:USDT | below_1h_threshold | +3.68% | +2.54% |
| USELESS/USDT:USDT | below_1h_threshold | +3.44% | +2.29% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
