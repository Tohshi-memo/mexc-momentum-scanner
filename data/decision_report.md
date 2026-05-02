# Decision Report

- generated_at: 2026-05-02T01:07:25.753057+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2848**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2848, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.30% | **-0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.73% | **+0.68%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.89% | **+1.23%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.40% | **+1.05%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.77% | **+0.97%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.16% | **+0.76%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.16% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RLS/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.02
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T01:07:24.093194+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=78270.9
- Funnel: target 755 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +80.55% | $23,327,808.32 |
| CHILLGUY/USDT:USDT | +13.50% | $1,023,864.45 |
| FIGHT/USDT:USDT | +12.00% | $1,276,738.94 |
| BLESS/USDT:USDT | +11.44% | $1,304,064.90 |
| B/USDT:USDT | +10.48% | $65,160,954.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +1.22% | +1.26% |
| TRB/USDT:USDT | below_1h_threshold | +1.07% | +1.11% |
| APE/USDT:USDT | below_1h_threshold | +1.05% | +1.10% |
| CHIP/USDT:USDT | below_1h_threshold | +0.89% | +0.93% |
| PHAROS/USDT:USDT | below_1h_threshold | +0.75% | +0.79% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
