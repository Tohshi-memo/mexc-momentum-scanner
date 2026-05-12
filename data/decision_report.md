# Decision Report

- generated_at: 2026-05-12T10:38:01.749509+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4110**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4110, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-1.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.52% | **-1.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.50% | **+0.15%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S | 8/18 | 44.4% | -1.42% | **-0.63%** |
| LIMIT_ATR | 16/20 | 80.0% | -1.00% | **-0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +3.40% | **+3.40%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.63% | **+1.97%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.42% | **+1.88%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.33% | **+1.67%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.43% | **+1.46%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$115.35** / 初期 $100.00 (+15.35%)
- 確定: 246件 (Win 68 / Loss 84 / Flat 94) / skip 425件
- 成長率目線: 平均log +0.000580 / 幾何平均 +0.058% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GIGA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $115.35

## 4. Latest Market Context

- 更新: 2026-05-12T10:37:57.863505+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=80664.8
- Funnel: target 762 → liquid 190 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.7 >= 65=1, 4h RSI 79.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GIGA/USDT:USDT | +63.68% | $5,130,620.79 |
| SAGA/USDT:USDT | +51.34% | $14,482,188.59 |
| SKYAI/USDT:USDT | +38.52% | $43,933,034.96 |
| USELESS/USDT:USDT | +33.69% | $8,310,850.43 |
| GUA/USDT:USDT | +29.11% | $3,338,586.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +3.44% | +3.61% |
| AIOT/USDT:USDT | below_1h_threshold | +2.74% | +2.90% |
| GIGA/USDT:USDT | below_1h_threshold | +2.72% | +2.89% |
| B/USDT:USDT | below_1h_threshold | +2.68% | +2.84% |
| CYS/USDT:USDT | below_1h_threshold | +2.45% | +2.61% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
