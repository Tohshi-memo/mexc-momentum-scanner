# Decision Report

- generated_at: 2026-05-12T08:37:59.994375+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4103**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4103, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.58% | **-0.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.56% | **+0.51%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_5PCT | 4/20 | 20.0% | +1.48% | **+0.30%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |
| LIMIT_1PCT | 19/20 | 95.0% | -0.44% | **-0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.43% | **+1.82%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +1.75% | **+1.75%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.84% | **+1.20%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.24% | **+1.12%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.79% | **+0.99%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$112.06** / 初期 $100.00 (+12.06%)
- 確定: 239件 (Win 63 / Loss 83 / Flat 93) / skip 425件
- 成長率目線: 平均log +0.000476 / 幾何平均 +0.048% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAHARA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $112.06

## 4. Latest Market Context

- 更新: 2026-05-12T08:37:53.679031+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=80918.4
- Funnel: target 761 → liquid 190 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GIGA/USDT:USDT | +40.91% | $3,566,423.52 |
| SAGA/USDT:USDT | +39.77% | $11,231,305.05 |
| SKYAI/USDT:USDT | +36.06% | $43,511,172.35 |
| USELESS/USDT:USDT | +33.37% | $6,391,470.90 |
| GUA/USDT:USDT | +31.50% | $2,436,358.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAHARA/USDT:USDT | below_1h_threshold | +4.67% | +4.53% |
| NAORIS/USDT:USDT | below_1h_threshold | +4.38% | +4.25% |
| H/USDT:USDT | below_1h_threshold | +3.49% | +3.36% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.40% | +3.27% |
| CHIP/USDT:USDT | below_1h_threshold | +2.47% | +2.34% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
