# Decision Report

- generated_at: 2026-05-02T22:42:03.175870+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2998**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.59% / filled 20/20。**
- 全期間 MARKET基準: n=2998, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +2.47% | **+0.62%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.67% | **+0.60%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.31% | **+1.31%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.10% | **+0.77%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.06% | **+0.58%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T22:42:01.438195+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=78630.0
- Funnel: target 755 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BIANRENSHENG/USDT:USDT | +14.51% | $1,247,395.90 |
| FHE/USDT:USDT | +14.40% | $1,265,785.37 |
| XNY/USDT:USDT | +12.92% | $2,110,086.28 |
| CHILLGUY/USDT:USDT | +10.92% | $1,127,824.67 |
| LUNC/USDT:USDT | +10.02% | $27,630,841.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLEND/USDT:USDT | below_1h_threshold | +2.72% | +2.80% |
| ZKSYNC/USDT:USDT | below_1h_threshold | +1.36% | +1.44% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +1.26% | +1.34% |
| PYTH/USDT:USDT | below_1h_threshold | +1.17% | +1.25% |
| VELO/USDT:USDT | below_1h_threshold | +1.15% | +1.23% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
