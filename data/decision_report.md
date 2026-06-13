# Decision Report

- generated_at: 2026-06-13T18:57:35.295742+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6603**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6603, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.43% | **+0.37%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.27% | **+0.20%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.05% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.45% | **+1.90%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.46% | **+1.17%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.33% | **+0.93%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.40% | **+0.84%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$167.15** / 初期 $100.00 (+67.15%)
- 確定: 1476件 (Win 396 / Loss 469 / Flat 611) / skip 1688件
- 成長率目線: 平均log +0.000348 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $167.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.60** / 初期 $100.00 (-0.40%)
- 確定: 14件 (Win 4 / Loss 5 / Flat 5) / skip 0件
- 成長率目線: 平均log -0.000285 / 幾何平均 -0.029% per trade / maxDD +1.05%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0258 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $99.60

## 5. Latest Market Context

- 更新: 2026-06-13T18:57:29.896681+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.26% price=64105.2
- Funnel: target 770 → liquid 137 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +26.11% | $69,916,570.22 |
| AT/USDT:USDT | +11.34% | $1,036,879.70 |
| RIF/USDT:USDT | +10.86% | $6,836,989.27 |
| H/USDT:USDT | +6.96% | $16,292,688.27 |
| COAI/USDT:USDT | +5.65% | $24,698,696.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +4.00% | +3.74% |
| ICP/USDT:USDT | below_1h_threshold | +3.46% | +3.20% |
| BTW/USDT:USDT | below_1h_threshold | +2.27% | +2.01% |
| LIT/USDT:USDT | below_1h_threshold | +1.50% | +1.25% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.39% | +1.13% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
