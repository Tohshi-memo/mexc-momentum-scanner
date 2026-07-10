# Decision Report

- generated_at: 2026-07-10T23:27:49.672589+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8531**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.73% / filled 20/20。**
- 全期間 MARKET基準: n=8531, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.73% | **+0.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.80% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.73% | **+0.73%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.04% | **+0.73%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.03% | **+0.67%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.15% | **+0.08%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.08% | **+0.04%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +0.02% | **+0.01%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$104.09** / 初期 $100.00 (+4.09%)
- 確定トレード: 83件 (TP 30 / SL 52 / EXP 1)
- 最新: NES/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.09
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$319.54** / 初期 $100.00 (+219.54%)
- 確定: 2719件 (Win 860 / Loss 912 / Flat 947) / skip 2373件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` EXPIRED account +0.13% 残高後 $319.54

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 642件 (Win 152 / Loss 159 / Flat 331) / skip 1300件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $105.11

## 5. Latest Market Context

- 更新: 2026-07-10T23:27:45.855416+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=0.0
- Funnel: target 0 → liquid 0 → pre 0 → checked 0 → surge 0 → strict 0

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
