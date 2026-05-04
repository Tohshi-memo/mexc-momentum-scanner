# Decision Report

- generated_at: 2026-05-04T01:17:14.819229+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3121**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3121, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.74% | **-0.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_BB3S | 5/19 | 26.3% | +0.72% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +4.80% | **+1.92%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.79% | **+1.43%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.16% | **+1.40%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.84% | **+1.20%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T01:17:12.745619+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=78422.2
- Funnel: target 756 → liquid 161 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +64.60% | $243,878,355.97 |
| SKYAI/USDT:USDT | +53.70% | $31,680,598.39 |
| TAG/USDT:USDT | +28.11% | $3,802,828.20 |
| GIGA/USDT:USDT | +25.65% | $1,080,746.51 |
| TRADOOR/USDT:USDT | +19.02% | $3,426,727.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +3.46% | +3.57% |
| TRADOOR/USDT:USDT | below_1h_threshold | +3.41% | +3.51% |
| BIO/USDT:USDT | below_1h_threshold | +2.55% | +2.65% |
| ON/USDT:USDT | below_1h_threshold | +1.56% | +1.66% |
| ORDI/USDT:USDT | below_1h_threshold | +1.30% | +1.40% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
