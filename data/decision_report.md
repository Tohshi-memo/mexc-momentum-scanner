# Decision Report

- generated_at: 2026-06-02T16:42:18.759254+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5467**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.28% / filled 20/20。**
- 全期間 MARKET基準: n=5467, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.43% | **+1.36%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_BB3S | 6/19 | 31.6% | +1.13% | **+0.36%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| ASK | 20/20 | 100.0% | +0.29% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +2.31% | **+1.73%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +2.17% | **+1.41%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.06% | **+0.53%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.51% | **+0.46%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.35% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$97.59** / 初期 $100.00 (-2.41%)
- 確定トレード: 88件 (TP 26 / SL 59 / EXP 3)
- 最新: STG/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.39** / 初期 $100.00 (+30.39%)
- 確定: 976件 (Win 229 / Loss 300 / Flat 447) / skip 1052件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $130.39

## 4. Latest Market Context

- 更新: 2026-06-02T16:42:12.511948+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.56% price=67652.8
- Funnel: target 773 → liquid 153 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=43, below_relative_strength=4, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.3 >= 65=1, 4h RSI 66.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ENA/USDT:USDT | +10.07% | $30,324,839.91 |
| USELESS/USDT:USDT | +6.87% | $4,901,415.04 |
| CHIP/USDT:USDT | +6.23% | $5,224,991.53 |
| ICP/USDT:USDT | +5.55% | $12,748,894.71 |
| PIEVERSE/USDT:USDT | +5.48% | $5,148,235.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ICP/USDT:USDT | below_relative_strength | +5.55% | +4.99% |
| PIEVERSE/USDT:USDT | below_relative_strength | +5.53% | +4.97% |
| LIT/USDT:USDT | below_relative_strength | +5.24% | +4.68% |
| APE/USDT:USDT | below_relative_strength | +5.10% | +4.53% |
| ZORA/USDT:USDT | below_1h_threshold | +4.97% | +4.41% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
