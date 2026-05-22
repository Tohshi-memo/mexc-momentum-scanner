# Decision Report

- generated_at: 2026-05-22T22:39:22.521788+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4742**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.84% / filled 20/20。**
- 全期間 MARKET基準: n=4742, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.84%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.51% | **+1.51%** |
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_10PCT | 3/20 | 15.0% | +2.30% | **+0.35%** |
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.82% | **+0.91%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.57% | **+0.51%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.78% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$96.20** / 初期 $100.00 (-3.80%)
- 確定トレード: 61件 (TP 16 / SL 42 / EXP 3)
- 最新: PLAY/USDT:USDT TP_HIT PnL +8.00% 残高後 $96.20
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.81** / 初期 $100.00 (+23.81%)
- 確定: 588件 (Win 149 / Loss 190 / Flat 249) / skip 715件
- 成長率目線: 平均log +0.000363 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $123.81

## 4. Latest Market Context

- 更新: 2026-05-22T22:39:20.504184+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=75720.2
- Funnel: target 764 → liquid 133 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +81.33% | $42,225,713.10 |
| BEAT/USDT:USDT | +15.25% | $45,137,299.49 |
| BILL/USDT:USDT | +14.97% | $16,600,067.92 |
| TAG/USDT:USDT | +10.76% | $1,014,711.18 |
| LAB/USDT:USDT | +3.82% | $29,215,814.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +3.70% | +3.99% |
| BILL/USDT:USDT | below_1h_threshold | +2.23% | +2.52% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.00% | +2.29% |
| BANANAS31/USDT:USDT | below_1h_threshold | +1.62% | +1.91% |
| NEX/USDT:USDT | below_1h_threshold | +1.35% | +1.64% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
