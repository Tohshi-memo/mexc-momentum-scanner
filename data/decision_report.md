# Decision Report

- generated_at: 2026-06-02T15:54:47.021062+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5463**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5463, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.33% | **+0.31%** |
| ASK | 20/20 | 100.0% | +0.22% | **+0.22%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_BB3S | 4/19 | 21.1% | +0.70% | **+0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.68% | **+1.01%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.54% | **+1.00%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.61% | **+0.40%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.29% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$97.59** / 初期 $100.00 (-2.41%)
- 確定トレード: 88件 (TP 26 / SL 59 / EXP 3)
- 最新: STG/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.71** / 初期 $100.00 (+31.71%)
- 確定: 974件 (Win 229 / Loss 298 / Flat 447) / skip 1050件
- 成長率目線: 平均log +0.000283 / 幾何平均 +0.028% per trade / maxDD +7.25%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $131.71

## 4. Latest Market Context

- 更新: 2026-06-02T15:54:41.343037+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.29% price=67113.6
- Funnel: target 773 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +41.56% | $5,492,120.79 |
| MRVLSTOCK/USDT:USDT | +32.11% | $10,229,253.04 |
| CLO/USDT:USDT | +27.64% | $1,609,973.06 |
| PIEVERSE/USDT:USDT | +27.35% | $4,955,336.55 |
| LAB/USDT:USDT | +26.49% | $177,569,395.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +4.80% | +6.09% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +3.08% | +4.37% |
| CLO/USDT:USDT | below_1h_threshold | +3.00% | +4.29% |
| ARMSTOCK/USDT:USDT | below_1h_threshold | +2.56% | +3.85% |
| LAB/USDT:USDT | below_1h_threshold | +2.45% | +3.74% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
