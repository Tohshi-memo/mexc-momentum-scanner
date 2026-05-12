# Decision Report

- generated_at: 2026-05-12T12:37:52.981856+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4117**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4117, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.74% | **-0.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.37% | **-0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.97% | **+1.48%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.43% | **+1.46%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.93% | **+1.16%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.09% | **+1.15%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.97% | **+0.82%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$115.64** / 初期 $100.00 (+15.64%)
- 確定: 253件 (Win 70 / Loss 87 / Flat 96) / skip 425件
- 成長率目線: 平均log +0.000574 / 幾何平均 +0.057% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $115.64

## 4. Latest Market Context

- 更新: 2026-05-12T12:37:49.676099+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=80874.9
- Funnel: target 763 → liquid 191 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +61.88% | $17,571,675.06 |
| GIGA/USDT:USDT | +51.17% | $6,428,133.68 |
| SKYAI/USDT:USDT | +40.30% | $44,183,440.78 |
| GUA/USDT:USDT | +33.01% | $3,528,560.10 |
| USELESS/USDT:USDT | +29.90% | $9,265,927.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STRK/USDT:USDT | below_1h_threshold | +4.04% | +3.87% |
| JELLYJELLY/USDT:USDT | below_1h_threshold | +3.02% | +2.86% |
| IRYS/USDT:USDT | below_1h_threshold | +2.77% | +2.60% |
| TWT/USDT:USDT | below_1h_threshold | +2.71% | +2.54% |
| GIGA/USDT:USDT | below_1h_threshold | +2.66% | +2.50% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
