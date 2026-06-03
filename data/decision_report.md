# Decision Report

- generated_at: 2026-06-03T03:03:04.604131+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5512**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.59% / filled 20/20。**
- 全期間 MARKET基準: n=5512, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| ASK | 20/20 | 100.0% | +0.67% | **+0.67%** |
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.52% | **+0.53%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| ASK_LONG | 20/20 | 100.0% | +0.42% | **+0.42%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | -0.28% | **-0.11%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.39** / 初期 $100.00 (+30.39%)
- 確定: 977件 (Win 229 / Loss 300 / Flat 448) / skip 1096件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $130.39

## 4. Latest Market Context

- 更新: 2026-06-03T03:03:01.458965+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=66577.3
- Funnel: target 773 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +35.86% | $13,647,446.49 |
| APR/USDT:USDT | +31.88% | $1,099,421.76 |
| GENIUS/USDT:USDT | +25.39% | $1,370,005.35 |
| LIT/USDT:USDT | +18.50% | $7,170,625.36 |
| BBSTOCK/USDT:USDT | +18.43% | $1,868,361.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +2.20% | +2.22% |
| ICP/USDT:USDT | below_1h_threshold | +1.23% | +1.24% |
| GENIUS/USDT:USDT | below_1h_threshold | +1.12% | +1.14% |
| NEAR/USDT:USDT | below_1h_threshold | +0.52% | +0.53% |
| GUN/USDT:USDT | below_1h_threshold | +0.41% | +0.43% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
