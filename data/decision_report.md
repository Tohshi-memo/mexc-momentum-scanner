# Decision Report

- generated_at: 2026-05-02T10:07:05.711169+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2892**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2892, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +3.63% | **+1.27%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.59% | **+0.88%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.52% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +5.22% | **+5.22%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +5.05% | **+3.28%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +4.49% | **+3.14%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +5.04% | **+2.27%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.21% | **+1.77%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T10:07:04.010570+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=78257.3
- Funnel: target 755 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +204.95% | $104,588,738.56 |
| TAC/USDT:USDT | +31.74% | $1,168,097.81 |
| BIO/USDT:USDT | +24.48% | $1,734,101.28 |
| KNC/USDT:USDT | +19.85% | $1,758,132.33 |
| SPACE/USDT:USDT | +19.41% | $1,010,628.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +2.84% | +2.83% |
| LAB/USDT:USDT | below_1h_threshold | +2.62% | +2.62% |
| RLS/USDT:USDT | below_1h_threshold | +1.58% | +1.58% |
| BSB/USDT:USDT | below_1h_threshold | +1.52% | +1.52% |
| COAI/USDT:USDT | below_1h_threshold | +0.61% | +0.60% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
