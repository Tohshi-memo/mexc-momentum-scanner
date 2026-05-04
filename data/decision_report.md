# Decision Report

- generated_at: 2026-05-04T03:07:15.005212+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3134**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3134, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.16% | **-1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 9/20 | 45.0% | +1.89% | **+0.85%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.95% | **+0.48%** |
| LIMIT_BB3S | 5/17 | 29.4% | +0.50% | **+0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.95% | **+2.21%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.11% | **+1.27%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.41% | **+1.26%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.39% | **+1.20%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.46% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T03:07:13.185982+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=80226.6
- Funnel: target 757 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +46.51% | $231,963,986.35 |
| TAG/USDT:USDT | +45.38% | $4,768,871.08 |
| SKYAI/USDT:USDT | +39.47% | $35,765,965.25 |
| GIGA/USDT:USDT | +30.04% | $1,111,578.51 |
| BSB/USDT:USDT | +28.57% | $14,839,141.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.37% | +3.25% |
| TAG/USDT:USDT | below_1h_threshold | +1.84% | +1.72% |
| BSB/USDT:USDT | below_1h_threshold | +1.46% | +1.34% |
| TST/USDT:USDT | below_1h_threshold | +1.38% | +1.27% |
| SIREN/USDT:USDT | below_1h_threshold | +1.13% | +1.01% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
