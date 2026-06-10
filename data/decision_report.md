# Decision Report

- generated_at: 2026-06-10T18:32:44.724535+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6238**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6238, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.97% | **-1.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_5PCT | 9/20 | 45.0% | -0.15% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +2.01% | **+2.01%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.51% | **+1.51%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +2.21% | **+0.78%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.10% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.74** / 初期 $100.00 (+49.74%)
- 確定: 1230件 (Win 307 / Loss 384 / Flat 539) / skip 1569件
- 成長率目線: 平均log +0.000328 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $149.74

## 4. Latest Market Context

- 更新: 2026-06-10T18:32:41.066422+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=61926.6
- Funnel: target 785 → liquid 152 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.2 >= 65=1, 4h RSI 85.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FOLKS/USDT:USDT | +18.71% | $6,294,074.26 |
| VELVET/USDT:USDT | +12.66% | $16,088,643.24 |
| BTW/USDT:USDT | +7.47% | $33,457,181.75 |
| BEAT/USDT:USDT | +5.42% | $116,921,368.21 |
| H/USDT:USDT | +5.39% | $17,903,447.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +4.43% | +4.45% |
| JCT/USDT:USDT | below_1h_threshold | +2.62% | +2.65% |
| BEAT/USDT:USDT | below_1h_threshold | +1.72% | +1.74% |
| WLFI/USDT:USDT | below_1h_threshold | +1.40% | +1.42% |
| MYX/USDT:USDT | below_1h_threshold | +0.80% | +0.82% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
