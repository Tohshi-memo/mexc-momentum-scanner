# Decision Report

- generated_at: 2026-09-13T03:21:44.752205+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14361**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14361, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.71% | **-0.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 6/20 | 30.0% | +3.28% | **+0.99%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.97% | **+0.79%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.27% | **+0.68%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.65% | **+0.42%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/13 | 53.8% | +6.42% | **+3.46%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +3.97% | **+1.59%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.21% | **+1.54%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +4.49% | **+1.35%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.00% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5430件 (Win 1635 / Loss 1760 / Flat 2035) / skip 5492件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$222.60** / 初期 $100.00 (+122.60%)
- 確定: 2879件 (Win 799 / Loss 672 / Flat 1408) / skip 4893件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0732 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: POWR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $222.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$127.47** / 初期 $100.00 (+27.47%)
- 確定: 2812件 (Win 838 / Loss 1080 / Flat 894) / pending 5件 / skip 3017件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000466 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: POWR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $127.47

## 6. Latest Market Context

- 更新: 2026-09-13T03:21:24.864706+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=77252.0
- Funnel: target 1068 → liquid 125 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 98.7 >= 65=1, 4h RSI 93.1 >= 65=1, 4h RSI 83.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +336.70% | $72,908,803.75 |
| POWR/USDT:USDT | +57.64% | $1,564,774.65 |
| ZCAT/USDT:USDT | +39.30% | $1,160,075.78 |
| LONGXIA/USDT:USDT | +21.15% | $9,816,648.03 |
| STORJ/USDT:USDT | +17.17% | $19,037,451.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +3.14% | +3.16% |
| NIULAI/USDT:USDT | below_1h_threshold | +2.68% | +2.70% |
| VTHO/USDT:USDT | below_1h_threshold | +2.02% | +2.03% |
| REZ/USDT:USDT | below_1h_threshold | +1.63% | +1.65% |
| STX/USDT:USDT | below_1h_threshold | +0.77% | +0.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
