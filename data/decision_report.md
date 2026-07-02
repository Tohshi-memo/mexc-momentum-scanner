# Decision Report

- generated_at: 2026-07-02T12:53:56.554033+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8078**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.83% / filled 20/20。**
- 全期間 MARKET基準: n=8078, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.83% | **+0.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.90% | **+0.90%** |
| MARKET | 20/20 | 100.0% | +0.83% | **+0.83%** |
| LIMIT_10PCT | 3/20 | 15.0% | +2.30% | **+0.35%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -0.07% | **-0.01%** |
| LIMIT_BB3S | 4/20 | 20.0% | -0.58% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.51% | **+1.28%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.02% | **+0.92%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.52% | **+0.61%** |
| ASK_LONG | 20/20 | 100.0% | +0.39% | **+0.39%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.44% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$104.18** / 初期 $100.00 (+4.18%)
- 確定トレード: 50件 (TP 19 / SL 30 / EXP 1)
- 最新: TAIKO/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.67** / 初期 $100.00 (+184.67%)
- 確定: 2444件 (Win 754 / Loss 816 / Flat 874) / skip 2195件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $284.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.14** / 初期 $100.00 (+5.14%)
- 確定: 556件 (Win 136 / Loss 131 / Flat 289) / skip 933件
- 成長率目線: 平均log +0.000090 / 幾何平均 +0.009% per trade / maxDD +3.53%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NOM/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $105.14

## 5. Latest Market Context

- 更新: 2026-07-02T12:53:45.625161+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=61440.3
- Funnel: target 834 → liquid 174 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.5 >= 65=1, 4h RSI 79.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BIRB/USDT:USDT | +65.49% | $7,667,217.54 |
| TLM/USDT:USDT | +64.23% | $13,827,889.50 |
| US/USDT:USDT | +38.84% | $1,679,226.99 |
| M/USDT:USDT | +35.94% | $5,962,484.39 |
| BREV/USDT:USDT | +28.52% | $5,885,864.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNI/USDT:USDT | below_1h_threshold | +4.33% | +4.16% |
| BIRB/USDT:USDT | below_1h_threshold | +4.01% | +3.83% |
| AERO/USDT:USDT | below_1h_threshold | +2.47% | +2.29% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.29% | +2.11% |
| APE/USDT:USDT | below_1h_threshold | +1.46% | +1.28% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
