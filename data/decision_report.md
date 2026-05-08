# Decision Report

- generated_at: 2026-05-08T15:52:35.985286+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3797**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.95% / filled 20/20。**
- 全期間 MARKET基準: n=3797, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.95% | **+1.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.07% | **+2.07%** |
| MARKET | 20/20 | 100.0% | +1.95% | **+1.95%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.58% | **+1.34%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.02% | **+0.66%** |
| LIMIT_3PCT | 9/20 | 45.0% | +1.24% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.91% | **+0.86%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.24% | **+0.62%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.39% | **+0.20%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | -0.08% | **-0.05%** |

## 2. $100 Live Portfolio

- 残高: **$98.82** / 初期 $100.00 (-1.18%)
- 確定トレード: 27件 (TP 7 / SL 18 / EXP 2)
- 最新: RKLBSTOCK/USDT:USDT SL_HIT PnL -2.88% 残高後 $98.82
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 192件 (Win 48 / Loss 64 / Flat 80) / skip 166件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FILECOIN/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T15:52:31.993377+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=80041.2
- Funnel: target 773 → liquid 181 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +55.88% | $15,856,084.47 |
| PHAROS/USDT:USDT | +44.05% | $13,535,057.16 |
| SPORTFUN/USDT:USDT | +38.16% | $1,096,125.88 |
| COLLECT/USDT:USDT | +32.73% | $1,335,318.65 |
| PLAY/USDT:USDT | +28.68% | $14,697,774.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STRK/USDT:USDT | below_1h_threshold | +4.30% | +4.40% |
| BILL/USDT:USDT | below_1h_threshold | +3.62% | +3.71% |
| SPORTFUN/USDT:USDT | below_1h_threshold | +3.02% | +3.11% |
| WLD/USDT:USDT | below_1h_threshold | +2.65% | +2.74% |
| JUP/USDT:USDT | below_1h_threshold | +2.54% | +2.63% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
