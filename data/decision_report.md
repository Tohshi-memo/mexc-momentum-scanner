# Decision Report

- generated_at: 2026-09-08T10:46:19.685805+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13982**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.09% / filled 20/20。**
- 全期間 MARKET基準: n=13982, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.09% | **+1.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.09% | **+1.09%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.95% | **+0.68%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.11% | **+0.11%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.44% | **+0.11%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | -0.44% | **-0.38%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,017.18** / 初期 $100.00 (+917.18%)
- 確定: 5248件 (Win 1584 / Loss 1705 / Flat 1959) / skip 5295件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: USELESS/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,017.18

## 4. Robust Adaptive DryRun ($100)

- 残高: **$189.74** / 初期 $100.00 (+89.74%)
- 確定: 2586件 (Win 721 / Loss 622 / Flat 1243) / skip 4807件
- 成長率目線: 平均log +0.000248 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0727 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_6PCT` TP_HIT account +0.69% 残高後 $189.74

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.66** / 初期 $100.00 (+21.66%)
- 確定: 2571件 (Win 755 / Loss 966 / Flat 850) / pending 4件 / skip 2878件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000149 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $121.66

## 6. Latest Market Context

- 更新: 2026-09-08T10:46:07.441182+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=78628.1
- Funnel: target 1065 → liquid 150 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +124.19% | $17,657,056.66 |
| BNCSTOCK/USDT:USDT | +46.99% | $1,713,582.99 |
| FORM/USDT:USDT | +25.04% | $4,007,672.24 |
| AERO/USDT:USDT | +14.88% | $6,082,412.75 |
| MEMEROBINHOOD/USDT:USDT | +13.77% | $5,957,051.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MEMEROBINHOOD/USDT:USDT | below_1h_threshold | +2.70% | +2.83% |
| UAI/USDT:USDT | below_1h_threshold | +1.85% | +1.98% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.28% | +1.41% |
| SOFTBANKSTOCK/USDT:USDT | below_1h_threshold | +1.19% | +1.32% |
| SEI/USDT:USDT | below_1h_threshold | +1.05% | +1.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
