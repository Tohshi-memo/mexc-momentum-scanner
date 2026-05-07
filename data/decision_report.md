# Decision Report

- generated_at: 2026-05-07T09:12:31.840298+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3604**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3604, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.47% | **-0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +5.42% | **+1.36%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.67% | **+0.33%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +3.84% | **+1.73%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.33% | **+1.05%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.32% | **+0.86%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.40% | **+0.84%** |
| MARKET_LONG | 20/20 | 100.0% | +0.84% | **+0.84%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.08** / 初期 $100.00 (+7.08%)
- 確定: 98件 (Win 34 / Loss 40 / Flat 24) / skip 67件
- 成長率目線: 平均log +0.000698 / 幾何平均 +0.070% per trade / maxDD +2.48%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SIREN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.76% 残高後 $107.08

## 4. Latest Market Context

- 更新: 2026-05-07T09:12:29.085194+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=81099.8
- Funnel: target 770 → liquid 185 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +195.55% | $2,027,251.95 |
| PENGUIN/USDT:USDT | +102.91% | $2,696,155.15 |
| B3/USDT:USDT | +87.09% | $10,489,465.01 |
| DOGS/USDT:USDT | +65.46% | $13,999,156.78 |
| D/USDT:USDT | +50.08% | $1,158,380.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PENGUIN/USDT:USDT | below_1h_threshold | +2.37% | +2.48% |
| DOGS/USDT:USDT | below_1h_threshold | +2.23% | +2.35% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.72% | +1.83% |
| B3/USDT:USDT | below_1h_threshold | +1.58% | +1.69% |
| LAB/USDT:USDT | below_1h_threshold | +1.56% | +1.67% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
