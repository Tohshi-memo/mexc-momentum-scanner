# Decision Report

- generated_at: 2026-05-09T01:02:43.970477+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3831**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3831, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-1.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.13% | **-1.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +1.04% | **+0.78%** |
| LIMIT_BB3S | 6/18 | 33.3% | +1.59% | **+0.53%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.45% | **+0.38%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.92% | **+1.34%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.21% | **+1.22%** |
| ASK_LONG | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.64% | **+0.74%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.79% | **+0.67%** |

## 2. $100 Live Portfolio

- 残高: **$98.33** / 初期 $100.00 (-1.67%)
- 確定トレード: 28件 (TP 7 / SL 19 / EXP 2)
- 最新: IO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.33
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 193件 (Win 48 / Loss 64 / Flat 81) / skip 199件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-09T01:02:40.983336+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=80183.8
- Funnel: target 767 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COLLECT/USDT:USDT | +24.71% | $6,257,511.97 |
| AKT/USDT:USDT | +13.93% | $1,673,090.80 |
| ICP/USDT:USDT | +13.80% | $228,082,055.89 |
| CORE/USDT:USDT | +13.69% | $1,721,286.57 |
| BIO/USDT:USDT | +13.19% | $1,123,075.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +2.30% | +2.31% |
| IP/USDT:USDT | below_1h_threshold | +1.50% | +1.52% |
| RAVE/USDT:USDT | below_1h_threshold | +1.46% | +1.47% |
| COLLECT/USDT:USDT | below_1h_threshold | +0.97% | +0.98% |
| XPL/USDT:USDT | below_1h_threshold | +0.72% | +0.73% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
