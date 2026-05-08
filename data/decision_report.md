# Decision Report

- generated_at: 2026-05-08T14:17:48.638539+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3789**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.93% / filled 20/20。**
- 全期間 MARKET基準: n=3789, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=+0.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.93% | **+0.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.05% | **+1.05%** |
| MARKET | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.37% | **+0.82%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +5.23% | **+5.23%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +3.00% | **+1.20%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.48% | **+0.74%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$98.82** / 初期 $100.00 (-1.18%)
- 確定トレード: 27件 (TP 7 / SL 18 / EXP 2)
- 最新: RKLBSTOCK/USDT:USDT SL_HIT PnL -2.88% 残高後 $98.82
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 191件 (Win 48 / Loss 64 / Flat 79) / skip 159件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHAROS/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T14:17:40.038307+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.49% price=80000.8
- Funnel: target 773 → liquid 181 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +49.35% | $12,983,907.06 |
| PHAROS/USDT:USDT | +48.78% | $12,409,571.41 |
| PLAY/USDT:USDT | +44.40% | $12,583,758.83 |
| COLLECT/USDT:USDT | +29.03% | $1,168,158.86 |
| AGT/USDT:USDT | +28.15% | $5,930,392.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IRENSTOCK/USDT:USDT | below_1h_threshold | +4.45% | +3.97% |
| RKLBSTOCK/USDT:USDT | below_1h_threshold | +4.44% | +3.95% |
| TST/USDT:USDT | below_1h_threshold | +3.19% | +2.70% |
| NOT/USDT:USDT | below_1h_threshold | +2.92% | +2.44% |
| CHIP/USDT:USDT | below_1h_threshold | +2.43% | +1.95% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
