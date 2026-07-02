# Decision Report

- generated_at: 2026-07-02T11:38:08.235239+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8069**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.60% / filled 20/20。**
- 全期間 MARKET基準: n=8069, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.63% | **+2.63%** |
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |
| LIMIT_10PCT | 3/20 | 15.0% | +2.30% | **+0.35%** |
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_9PCT_LONG | 9/20 | 45.0% | +1.30% | **+0.58%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +0.19% | **+0.12%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +0.03% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$103.14** / 初期 $100.00 (+3.14%)
- 確定トレード: 49件 (TP 18 / SL 30 / EXP 1)
- 最新: NOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.67** / 初期 $100.00 (+184.67%)
- 確定: 2444件 (Win 754 / Loss 816 / Flat 874) / skip 2186件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $284.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.14** / 初期 $100.00 (+5.14%)
- 確定: 556件 (Win 136 / Loss 131 / Flat 289) / skip 924件
- 成長率目線: 平均log +0.000090 / 幾何平均 +0.009% per trade / maxDD +3.53%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NOM/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $105.14

## 5. Latest Market Context

- 更新: 2026-07-02T11:37:54.555913+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=61252.7
- Funnel: target 834 → liquid 168 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TLM/USDT:USDT | +73.97% | $10,104,869.88 |
| BIRB/USDT:USDT | +63.29% | $7,198,381.52 |
| BREV/USDT:USDT | +40.97% | $4,942,684.50 |
| SYN/USDT:USDT | +33.54% | $21,602,394.62 |
| US/USDT:USDT | +29.11% | $1,274,535.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNI/USDT:USDT | below_1h_threshold | +4.39% | +4.36% |
| BIRB/USDT:USDT | below_1h_threshold | +3.82% | +3.79% |
| ZEC/USDT:USDT | below_1h_threshold | +3.80% | +3.78% |
| JUP/USDT:USDT | below_1h_threshold | +2.09% | +2.07% |
| COOKIE/USDT:USDT | below_1h_threshold | +1.35% | +1.33% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
