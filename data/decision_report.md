# Decision Report

- generated_at: 2026-05-02T04:07:01.195037+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2859**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2859, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-2.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.02% | **-2.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.00% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +4.03% | **+2.22%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.91% | **+1.74%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.14% | **+1.73%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.84% | **+1.47%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 7件 (TP 4 / SL 3 / EXP 0)
- 最新: BIO/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T04:06:59.436982+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=78285.8
- Funnel: target 755 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +111.01% | $35,223,058.09 |
| SKYAI/USDT:USDT | +19.19% | $21,295,538.37 |
| B/USDT:USDT | +15.63% | $72,028,480.94 |
| BLESS/USDT:USDT | +14.49% | $1,824,652.86 |
| PLAY/USDT:USDT | +8.65% | $4,479,932.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.79% | +3.91% |
| B/USDT:USDT | below_1h_threshold | +2.28% | +2.40% |
| LAB/USDT:USDT | below_1h_threshold | +2.18% | +2.29% |
| LYN/USDT:USDT | below_1h_threshold | +1.04% | +1.15% |
| FIGHT/USDT:USDT | below_1h_threshold | +0.83% | +0.94% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
