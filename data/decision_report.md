# Decision Report

- generated_at: 2026-05-08T10:32:29.720076+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3771**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.54% / filled 20/20。**
- 全期間 MARKET基準: n=3771, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=+2.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.54% | **+2.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.54% | **+2.54%** |
| ASK | 20/20 | 100.0% | +2.45% | **+2.45%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.94% | **+1.65%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.80% | **+0.52%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.19% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +1.19% | **+0.68%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | -0.89% | **-0.18%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -1.03% | **-0.21%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -1.45% | **-0.29%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | -0.56% | **-0.45%** |

## 2. $100 Live Portfolio

- 残高: **$99.32** / 初期 $100.00 (-0.68%)
- 確定トレード: 26件 (TP 7 / SL 17 / EXP 2)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 191件 (Win 48 / Loss 64 / Flat 79) / skip 141件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHAROS/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T10:32:26.507054+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=79893.7
- Funnel: target 773 → liquid 182 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHAROS/USDT:USDT | +43.97% | $6,685,044.18 |
| PLAY/USDT:USDT | +34.00% | $9,218,082.77 |
| BSB/USDT:USDT | +33.81% | $9,148,963.75 |
| STRK/USDT:USDT | +31.43% | $18,249,828.90 |
| AGT/USDT:USDT | +24.01% | $5,499,357.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PHAROS/USDT:USDT | below_1h_threshold | +4.42% | +4.33% |
| CHIP/USDT:USDT | below_1h_threshold | +3.75% | +3.67% |
| ONDO/USDT:USDT | below_1h_threshold | +2.61% | +2.53% |
| STRK/USDT:USDT | below_1h_threshold | +1.97% | +1.89% |
| NOT/USDT:USDT | below_1h_threshold | +1.40% | +1.31% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
