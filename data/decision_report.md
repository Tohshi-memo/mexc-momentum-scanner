# Decision Report

- generated_at: 2026-05-02T18:47:06.834953+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2971**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.48% / filled 20/20。**
- 全期間 MARKET基準: n=2971, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.38% | **+1.38%** |
| LIMIT_BB3S | 4/12 | 33.3% | +2.09% | **+0.70%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.77% | **+0.69%** |
| ASK | 20/20 | 100.0% | +0.54% | **+0.54%** |
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.80% | **+0.72%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.17% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$102.70** / 初期 $100.00 (+2.70%)
- 確定トレード: 9件 (TP 4 / SL 4 / EXP 1)
- 最新: RAVE/USDT:USDT EXPIRED PnL +5.55% 残高後 $102.70
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T18:47:02.087052+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=78406.2
- Funnel: target 755 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +24.57% | $8,985,008.46 |
| TAC/USDT:USDT | +9.01% | $2,624,956.44 |
| BIANRENSHENG/USDT:USDT | +6.77% | $1,057,574.40 |
| BASED/USDT:USDT | +5.39% | $1,346,734.00 |
| PNUT/USDT:USDT | +5.38% | $1,648,697.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BABY/USDT:USDT | below_1h_threshold | +4.24% | +4.18% |
| AIOT/USDT:USDT | below_1h_threshold | +3.74% | +3.69% |
| RLS/USDT:USDT | below_1h_threshold | +2.86% | +2.80% |
| BR/USDT:USDT | below_1h_threshold | +2.83% | +2.77% |
| CYS/USDT:USDT | below_1h_threshold | +2.73% | +2.67% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
