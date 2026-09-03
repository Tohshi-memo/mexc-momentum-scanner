# Decision Report

- generated_at: 2026-09-03T12:46:36.114056+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13473**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13473, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.28% | **-2.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.27% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.74% | **+2.33%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +4.18% | **+1.88%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.22% | **+1.33%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.12% | **+0.96%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5008件 (Win 1516 / Loss 1644 / Flat 1848) / skip 5026件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BONER/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.36% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$184.60** / 初期 $100.00 (+84.60%)
- 確定: 2373件 (Win 671 / Loss 576 / Flat 1126) / skip 4511件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1795 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $184.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.66** / 初期 $100.00 (+15.66%)
- 確定: 2167件 (Win 642 / Loss 849 / Flat 676) / pending 6件 / skip 2775件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000387 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BONER/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $115.66

## 6. Latest Market Context

- 更新: 2026-09-03T12:46:21.889311+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.41% price=78229.0
- Funnel: target 1048 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MARSCOIN/USDT:USDT | +90.42% | $8,208,850.26 |
| BR/USDT:USDT | +45.31% | $4,387,195.35 |
| EDGE/USDT:USDT | +44.44% | $6,397,413.00 |
| PONS/USDT:USDT | +41.56% | $6,105,981.11 |
| BONER/USDT:USDT | +35.87% | $2,323,015.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_relative_strength | +5.06% | +4.65% |
| CHIP/USDT:USDT | below_1h_threshold | +4.28% | +3.87% |
| EDGE/USDT:USDT | below_1h_threshold | +4.21% | +3.80% |
| NIULAI/USDT:USDT | below_1h_threshold | +4.18% | +3.77% |
| XPL/USDT:USDT | below_1h_threshold | +2.31% | +1.90% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
