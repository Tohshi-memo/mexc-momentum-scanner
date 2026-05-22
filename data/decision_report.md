# Decision Report

- generated_at: 2026-05-22T14:47:56.403121+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4709**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4709, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| ASK | 20/20 | 100.0% | +0.39% | **+0.39%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.61% | **+0.36%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.43% | **+0.28%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +0.46% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.66** / 初期 $100.00 (+21.66%)
- 確定: 564件 (Win 144 / Loss 186 / Flat 234) / skip 706件
- 成長率目線: 平均log +0.000348 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BUILDONBOB/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $121.66

## 4. Latest Market Context

- 更新: 2026-05-22T14:47:53.917840+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.64% price=76759.3
- Funnel: target 768 → liquid 139 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BUILDONBOB/USDT:USDT | +73.23% | $4,496,729.03 |
| BEAT/USDT:USDT | +42.46% | $24,417,594.89 |
| GENIUS/USDT:USDT | +42.00% | $3,772,654.46 |
| ALT/USDT:USDT | +32.49% | $3,320,165.16 |
| AGT/USDT:USDT | +29.79% | $1,023,443.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARMSTOCK/USDT:USDT | below_1h_threshold | +3.34% | +3.99% |
| EDEN/USDT:USDT | below_1h_threshold | +3.12% | +3.76% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.90% | +2.54% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +1.65% | +2.29% |
| VVV/USDT:USDT | below_1h_threshold | +1.47% | +2.12% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
