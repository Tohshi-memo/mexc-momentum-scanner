# Decision Report

- generated_at: 2026-06-12T05:07:20.404473+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6461**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6461, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.98% | **-0.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.33% | **+0.58%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.55% | **+0.42%** |
| LIMIT_BB3S | 2/18 | 11.1% | +2.90% | **+0.32%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.20% | **+1.65%** |
| ASK_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.03% | **+0.93%** |
| MARKET_LONG | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$95.65** / 初期 $100.00 (-4.35%)
- 確定トレード: 16件 (TP 2 / SL 13 / EXP 1)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $95.65
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$155.23** / 初期 $100.00 (+55.23%)
- 確定: 1336件 (Win 351 / Loss 429 / Flat 556) / skip 1686件
- 成長率目線: 平均log +0.000329 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $155.23

## 4. Latest Market Context

- 更新: 2026-06-12T05:07:14.755144+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=63619.9
- Funnel: target 783 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +72.58% | $139,367,905.35 |
| XPL/USDT:USDT | +34.54% | $6,152,828.44 |
| NAORIS/USDT:USDT | +28.62% | $1,713,206.72 |
| H/USDT:USDT | +28.41% | $39,364,481.78 |
| SKYAI/USDT:USDT | +22.95% | $14,080,419.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +3.35% | +3.43% |
| VELVET/USDT:USDT | below_1h_threshold | +2.35% | +2.43% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.61% | +1.69% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.80% | +0.88% |
| PAYPSTOCK/USDT:USDT | below_1h_threshold | +0.62% | +0.70% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
