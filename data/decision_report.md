# Decision Report

- generated_at: 2026-06-13T18:38:18.496225+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6599**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6599, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.05% | **+0.01%** |
| LIMIT_3PCT | 18/20 | 90.0% | -0.14% | **-0.13%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.25% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.89% | **+2.02%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +3.06% | **+1.84%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +3.64% | **+1.64%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.41% | **+1.08%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$169.68** / 初期 $100.00 (+69.68%)
- 確定: 1472件 (Win 396 / Loss 466 / Flat 610) / skip 1688件
- 成長率目線: 平均log +0.000359 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $169.68

## 4. Robust Adaptive DryRun ($100)

- 残高: **$100.65** / 初期 $100.00 (+0.65%)
- 確定: 10件 (Win 4 / Loss 2 / Flat 4) / skip 0件
- 成長率目線: 平均log +0.000653 / 幾何平均 +0.065% per trade / maxDD +0.35%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0690 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $100.65

## 5. Latest Market Context

- 更新: 2026-06-13T18:38:13.055712+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.42% price=64206.1
- Funnel: target 770 → liquid 136 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +30.01% | $65,445,554.71 |
| AT/USDT:USDT | +12.26% | $1,025,697.09 |
| RIF/USDT:USDT | +9.14% | $6,586,358.15 |
| H/USDT:USDT | +7.02% | $15,992,956.55 |
| SKYAI/USDT:USDT | +3.72% | $18,723,549.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BRETT/USDT:USDT | below_1h_threshold | +2.09% | +1.67% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.74% | +1.32% |
| ICP/USDT:USDT | below_1h_threshold | +1.63% | +1.21% |
| SPACE/USDT:USDT | below_1h_threshold | +1.49% | +1.07% |
| EDGE/USDT:USDT | below_1h_threshold | +1.40% | +0.98% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
