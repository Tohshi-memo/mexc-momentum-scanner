# Decision Report

- generated_at: 2026-05-08T13:17:34.686041+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3784**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.42% / filled 20/20。**
- 全期間 MARKET基準: n=3784, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=+1.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.42% | **+1.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.45% | **+1.45%** |
| MARKET | 20/20 | 100.0% | +1.42% | **+1.42%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.80% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +8.00% | **+4.00%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.41% | **+0.70%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$99.32** / 初期 $100.00 (-0.68%)
- 確定トレード: 26件 (TP 7 / SL 17 / EXP 2)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 191件 (Win 48 / Loss 64 / Flat 79) / skip 154件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHAROS/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T13:17:31.859122+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=79766.0
- Funnel: target 773 → liquid 184 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHAROS/USDT:USDT | +47.01% | $11,576,710.94 |
| BSB/USDT:USDT | +40.87% | $11,973,646.25 |
| PLAY/USDT:USDT | +39.09% | $11,644,374.42 |
| COLLECT/USDT:USDT | +27.51% | $1,078,262.28 |
| AGT/USDT:USDT | +26.69% | $5,819,141.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +2.95% | +3.23% |
| PLAY/USDT:USDT | below_1h_threshold | +2.76% | +3.04% |
| TIA/USDT:USDT | below_1h_threshold | +1.51% | +1.79% |
| GALA/USDT:USDT | below_1h_threshold | +1.43% | +1.70% |
| CHIP/USDT:USDT | below_1h_threshold | +0.76% | +1.04% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
