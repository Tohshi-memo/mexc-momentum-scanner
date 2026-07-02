# Decision Report

- generated_at: 2026-07-02T12:44:14.752131+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8077**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.68% / filled 20/20。**
- 全期間 MARKET基準: n=8077, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.68% | **+0.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.73% | **+0.73%** |
| MARKET | 20/20 | 100.0% | +0.68% | **+0.68%** |
| LIMIT_10PCT | 4/20 | 20.0% | +3.09% | **+0.62%** |
| LIMIT_9PCT | 4/20 | 20.0% | +0.29% | **+0.06%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -0.07% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.24% | **+1.01%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.10% | **+0.93%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.69% | **+0.62%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.94% | **+0.56%** |
| ASK_LONG | 20/20 | 100.0% | +0.16% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$104.18** / 初期 $100.00 (+4.18%)
- 確定トレード: 50件 (TP 19 / SL 30 / EXP 1)
- 最新: TAIKO/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.67** / 初期 $100.00 (+184.67%)
- 確定: 2444件 (Win 754 / Loss 816 / Flat 874) / skip 2194件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $284.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.14** / 初期 $100.00 (+5.14%)
- 確定: 556件 (Win 136 / Loss 131 / Flat 289) / skip 932件
- 成長率目線: 平均log +0.000090 / 幾何平均 +0.009% per trade / maxDD +3.53%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NOM/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $105.14

## 5. Latest Market Context

- 更新: 2026-07-02T12:44:05.158333+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=61378.3
- Funnel: target 834 → liquid 173 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TLM/USDT:USDT | +72.86% | $13,479,641.28 |
| BIRB/USDT:USDT | +60.85% | $7,590,835.75 |
| M/USDT:USDT | +33.08% | $5,898,024.67 |
| US/USDT:USDT | +32.19% | $1,494,272.20 |
| BREV/USDT:USDT | +28.97% | $5,854,160.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +4.14% | +4.06% |
| US/USDT:USDT | below_1h_threshold | +3.18% | +3.11% |
| UNI/USDT:USDT | below_1h_threshold | +2.96% | +2.88% |
| SPX/USDT:USDT | below_1h_threshold | +2.17% | +2.10% |
| BEAT/USDT:USDT | below_1h_threshold | +1.58% | +1.51% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
