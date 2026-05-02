# Decision Report

- generated_at: 2026-05-02T19:17:02.028977+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2974**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.15% / filled 20/20。**
- 全期間 MARKET基準: n=2974, expectancy=-0.16%
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
| LIMIT_1PCT | 18/20 | 90.0% | +1.28% | **+1.16%** |
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_BB3S | 4/13 | 30.8% | +2.47% | **+0.76%** |
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

- 更新: 2026-05-02T19:17:00.175873+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=78439.7
- Funnel: target 755 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +12.11% | $10,091,095.71 |
| TAC/USDT:USDT | +8.00% | $2,613,252.92 |
| LUNC/USDT:USDT | +6.23% | $23,230,290.90 |
| BIANRENSHENG/USDT:USDT | +5.85% | $1,079,180.68 |
| BASED/USDT:USDT | +5.06% | $1,298,272.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.04% | +4.03% |
| LUNC/USDT:USDT | below_1h_threshold | +2.98% | +2.97% |
| XNY/USDT:USDT | below_1h_threshold | +2.29% | +2.28% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.85% | +1.84% |
| SPACE/USDT:USDT | below_1h_threshold | +1.43% | +1.42% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
