# Decision Report

- generated_at: 2026-05-02T02:17:14.928983+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2851**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.20% / filled 20/20。**
- 全期間 MARKET基準: n=2851, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.61% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.27% | **+0.82%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.30% | **+0.78%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.92% | **+0.77%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.99% | **+0.74%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RLS/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.02
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T02:17:13.224423+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=78270.9
- Funnel: target 755 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +63.71% | $28,523,771.30 |
| BLESS/USDT:USDT | +16.93% | $1,478,306.14 |
| SKYAI/USDT:USDT | +15.21% | $21,587,146.93 |
| FIGHT/USDT:USDT | +10.72% | $1,079,613.18 |
| B/USDT:USDT | +9.54% | $67,302,938.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +2.75% | +2.78% |
| BLESS/USDT:USDT | below_1h_threshold | +2.22% | +2.25% |
| FIGHT/USDT:USDT | below_1h_threshold | +1.51% | +1.54% |
| RAVE/USDT:USDT | below_1h_threshold | +1.02% | +1.05% |
| TAG/USDT:USDT | below_1h_threshold | +0.78% | +0.81% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
