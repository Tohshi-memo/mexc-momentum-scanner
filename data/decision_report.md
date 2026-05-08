# Decision Report

- generated_at: 2026-05-08T15:27:39.684008+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3795**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.92% / filled 20/20。**
- 全期間 MARKET基準: n=3795, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.92% | **+1.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.03% | **+2.03%** |
| MARKET | 20/20 | 100.0% | +1.92% | **+1.92%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.20% | **+0.96%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.16% | **+0.58%** |
| LIMIT_3PCT | 9/20 | 45.0% | +1.16% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.91% | **+0.86%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.24% | **+0.62%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.39% | **+0.20%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.14% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$98.82** / 初期 $100.00 (-1.18%)
- 確定トレード: 27件 (TP 7 / SL 18 / EXP 2)
- 最新: RKLBSTOCK/USDT:USDT SL_HIT PnL -2.88% 残高後 $98.82
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 191件 (Win 48 / Loss 64 / Flat 79) / skip 165件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHAROS/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T15:27:36.453750+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.60% price=79634.3
- Funnel: target 773 → liquid 179 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +55.29% | $14,755,194.38 |
| PHAROS/USDT:USDT | +48.60% | $13,243,527.08 |
| COLLECT/USDT:USDT | +33.16% | $1,301,394.15 |
| PLAY/USDT:USDT | +30.77% | $14,180,609.20 |
| AGT/USDT:USDT | +28.51% | $5,998,754.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PHAROS/USDT:USDT | below_1h_threshold | +3.30% | +3.90% |
| BILL/USDT:USDT | below_1h_threshold | +3.14% | +3.74% |
| SATO/USDT:USDT | below_1h_threshold | +3.12% | +3.72% |
| STRK/USDT:USDT | below_1h_threshold | +2.11% | +2.71% |
| RKLBSTOCK/USDT:USDT | below_1h_threshold | +1.41% | +2.00% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
