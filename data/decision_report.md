# Decision Report

- generated_at: 2026-05-08T05:27:53.815209+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3737**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.34% / filled 20/20。**
- 全期間 MARKET基準: n=3737, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+1.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.34% | **+1.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.34% | **+1.34%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.51% | **+1.28%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.26% | **+1.01%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.96% | **+0.98%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.32% | **+0.86%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.95% | **+0.88%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.41% | **+0.71%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.59% | **+0.35%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.40% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$98.83** / 初期 $100.00 (-1.17%)
- 確定トレード: 24件 (TP 6 / SL 16 / EXP 2)
- 最新: PENGUIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 190件 (Win 48 / Loss 64 / Flat 78) / skip 108件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +3.48%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T05:27:50.661386+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=79583.0
- Funnel: target 772 → liquid 181 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +34.85% | $2,794,109.42 |
| BSB/USDT:USDT | +24.06% | $3,967,236.40 |
| SATO/USDT:USDT | +23.63% | $8,675,453.93 |
| LAB/USDT:USDT | +19.91% | $212,557,528.79 |
| NOT/USDT:USDT | +19.69% | $10,430,332.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.18% | +4.22% |
| PLAY/USDT:USDT | below_1h_threshold | +3.81% | +3.85% |
| NOT/USDT:USDT | below_1h_threshold | +2.33% | +2.37% |
| HIGH/USDT:USDT | below_1h_threshold | +2.28% | +2.32% |
| CHIP/USDT:USDT | below_1h_threshold | +1.68% | +1.73% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
