# Decision Report

- generated_at: 2026-05-08T11:22:39.435190+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3776**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.78% / filled 20/20。**
- 全期間 MARKET基準: n=3776, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=+1.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.78% | **+1.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.78% | **+1.78%** |
| ASK | 20/20 | 100.0% | +1.69% | **+1.69%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.10% | **+0.93%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.08% | **+0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +2.15% | **+1.23%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.49% | **+0.42%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.45% | **+0.36%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$99.32** / 初期 $100.00 (-0.68%)
- 確定トレード: 26件 (TP 7 / SL 17 / EXP 2)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 191件 (Win 48 / Loss 64 / Flat 79) / skip 146件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHAROS/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T11:22:36.393839+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=80204.1
- Funnel: target 773 → liquid 181 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHAROS/USDT:USDT | +51.91% | $7,887,533.42 |
| BSB/USDT:USDT | +38.81% | $9,858,316.00 |
| AGT/USDT:USDT | +29.08% | $5,655,349.13 |
| STRK/USDT:USDT | +25.80% | $22,080,194.93 |
| CHIP/USDT:USDT | +25.03% | $34,284,893.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHIP/USDT:USDT | below_1h_threshold | +4.59% | +4.53% |
| PHAROS/USDT:USDT | below_1h_threshold | +4.54% | +4.49% |
| SIREN/USDT:USDT | below_1h_threshold | +2.88% | +2.83% |
| BSB/USDT:USDT | below_1h_threshold | +2.53% | +2.47% |
| ONDO/USDT:USDT | below_1h_threshold | +2.26% | +2.20% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
