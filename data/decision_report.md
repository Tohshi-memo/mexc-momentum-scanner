# Decision Report

- generated_at: 2026-05-02T18:57:05.187485+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2973**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.15% / filled 20/20。**
- 全期間 MARKET基準: n=2973, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+1.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.21% | **+1.21%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.34% | **+1.21%** |
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_BB3S | 4/12 | 33.3% | +2.47% | **+0.82%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.58% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +5.04% | **+1.51%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +2.60% | **+0.91%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.65% | **+0.29%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.21% | **+0.09%** |

## 2. $100 Live Portfolio

- 残高: **$102.70** / 初期 $100.00 (+2.70%)
- 確定トレード: 9件 (TP 4 / SL 4 / EXP 1)
- 最新: RAVE/USDT:USDT EXPIRED PnL +5.55% 残高後 $102.70
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T18:56:58.835216+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=78446.0
- Funnel: target 755 → liquid 167 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAC/USDT:USDT | +8.10% | $2,635,655.17 |
| BSB/USDT:USDT | +6.73% | $9,789,064.12 |
| BIANRENSHENG/USDT:USDT | +6.06% | $1,067,758.88 |
| BASED/USDT:USDT | +5.11% | $1,357,416.65 |
| PNUT/USDT:USDT | +5.06% | $1,681,175.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BABY/USDT:USDT | below_relative_strength | +5.03% | +4.92% |
| TAO/USDT:USDT | below_1h_threshold | +2.88% | +2.77% |
| RLS/USDT:USDT | below_1h_threshold | +2.76% | +2.66% |
| PENDLE/USDT:USDT | below_1h_threshold | +2.66% | +2.55% |
| CHILLGUY/USDT:USDT | below_1h_threshold | +2.25% | +2.14% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
