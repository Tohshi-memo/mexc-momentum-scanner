# Decision Report

- generated_at: 2026-05-02T06:03:37.266305+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2871**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2871, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_BB3S | 7/18 | 38.9% | +2.31% | **+0.90%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.56% | **+0.56%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.84% | **+1.57%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.11% | **+0.72%** |
| ASK_LONG | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.10% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 7件 (TP 4 / SL 3 / EXP 0)
- 最新: BIO/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T06:03:35.452320+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=78218.4
- Funnel: target 755 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +205.65% | $57,649,168.60 |
| PLAY/USDT:USDT | +21.79% | $4,712,079.89 |
| BLESS/USDT:USDT | +14.42% | $2,046,329.49 |
| SKYAI/USDT:USDT | +12.86% | $20,800,638.66 |
| B/USDT:USDT | +10.82% | $77,208,700.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.61% | +4.51% |
| FIGHT/USDT:USDT | below_1h_threshold | +1.36% | +1.26% |
| USTC/USDT:USDT | below_1h_threshold | +1.25% | +1.15% |
| BLESS/USDT:USDT | below_1h_threshold | +1.15% | +1.05% |
| VELVET/USDT:USDT | below_1h_threshold | +1.01% | +0.91% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
