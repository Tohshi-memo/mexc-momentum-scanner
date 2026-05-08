# Decision Report

- generated_at: 2026-05-08T12:42:43.825667+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3783**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.84% / filled 20/20。**
- 全期間 MARKET基準: n=3783, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=+1.84%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.84% | **+1.84%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.87% | **+1.87%** |
| MARKET | 20/20 | 100.0% | +1.84% | **+1.84%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.75% | **+0.60%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +4.00% | **+2.40%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.69% | **+0.34%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$99.32** / 初期 $100.00 (-0.68%)
- 確定トレード: 26件 (TP 7 / SL 17 / EXP 2)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 191件 (Win 48 / Loss 64 / Flat 79) / skip 153件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHAROS/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T12:42:40.854767+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=80179.0
- Funnel: target 773 → liquid 184 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.2 >= 65=1, 4h RSI 73.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHAROS/USDT:USDT | +50.52% | $10,862,558.59 |
| BSB/USDT:USDT | +44.29% | $11,558,380.75 |
| PLAY/USDT:USDT | +34.13% | $11,244,572.48 |
| STRK/USDT:USDT | +26.90% | $25,715,896.29 |
| AGT/USDT:USDT | +26.80% | $5,799,201.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LUNC/USDT:USDT | below_1h_threshold | +4.54% | +4.54% |
| SATO/USDT:USDT | below_1h_threshold | +2.85% | +2.85% |
| GALA/USDT:USDT | below_1h_threshold | +2.59% | +2.59% |
| IRENSTOCK/USDT:USDT | below_1h_threshold | +2.20% | +2.20% |
| PENDLE/USDT:USDT | below_1h_threshold | +2.13% | +2.13% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
