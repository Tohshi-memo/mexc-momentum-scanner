# Decision Report

- generated_at: 2026-08-26T09:56:27.141585+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12692**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12692, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +0.67% | **+0.34%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.70% | **+2.43%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.99% | **+2.24%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.10% | **+1.55%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +1.43% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$706.69** / 初期 $100.00 (+606.69%)
- 確定: 4594件 (Win 1398 / Loss 1508 / Flat 1688) / skip 4659件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $706.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$159.03** / 初期 $100.00 (+59.03%)
- 確定: 1989件 (Win 542 / Loss 475 / Flat 972) / skip 4114件
- 成長率目線: 平均log +0.000233 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1721 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $159.03

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.93** / 初期 $100.00 (+16.93%)
- 確定: 1967件 (Win 578 / Loss 748 / Flat 641) / pending 6件 / skip 2195件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000507 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TAC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $116.93

## 6. Latest Market Context

- 更新: 2026-08-26T09:56:15.709841+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.32% price=78419.1
- Funnel: target 1023 → liquid 170 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.5 >= 65=1, 4h RSI 67.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +171.41% | $12,935,333.16 |
| BMT/USDT:USDT | +52.44% | $14,024,615.93 |
| TAC/USDT:USDT | +49.31% | $6,152,892.91 |
| LONGXIA/USDT:USDT | +26.55% | $1,967,714.71 |
| PORTAL/USDT:USDT | +21.51% | $4,010,371.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PORTAL/USDT:USDT | below_1h_threshold | +3.01% | +3.33% |
| CHIP/USDT:USDT | below_1h_threshold | +2.25% | +2.57% |
| BR/USDT:USDT | below_1h_threshold | +1.25% | +1.57% |
| HEI/USDT:USDT | below_1h_threshold | +1.21% | +1.54% |
| BEAT/USDT:USDT | below_1h_threshold | +1.17% | +1.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
