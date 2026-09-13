# Decision Report

- generated_at: 2026-09-13T03:46:41.914637+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14371**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14371, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-3.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -3.40% | **-3.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 10/20 | 50.0% | +0.37% | **+0.19%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.56% | **+0.06%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | -1.00% | **-0.20%** |
| LIMIT_6PCT | 12/20 | 60.0% | -0.51% | **-0.31%** |
| LIMIT_10PCT | 8/20 | 40.0% | -1.00% | **-0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +2.77% | **+2.77%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.80% | **+2.28%** |
| LIMIT_BB3S_LONG | 5/11 | 45.5% | +5.02% | **+2.28%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.15% | **+1.61%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.20% | **+1.60%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5430件 (Win 1635 / Loss 1760 / Flat 2035) / skip 5502件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$222.90** / 初期 $100.00 (+122.90%)
- 確定: 2889件 (Win 802 / Loss 677 / Flat 1410) / skip 4893件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $222.90

## 5. Causal Adaptive DryRun ($100)

- 残高: **$127.56** / 初期 $100.00 (+27.56%)
- 確定: 2821件 (Win 841 / Loss 1085 / Flat 895) / pending 5件 / skip 3018件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000460 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $127.56

## 6. Latest Market Context

- 更新: 2026-09-13T03:46:21.835182+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=77188.4
- Funnel: target 1068 → liquid 127 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 99.2 >= 65=1, 4h RSI 73.4 >= 65=1, 4h RSI 83.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +547.37% | $77,798,608.48 |
| POWR/USDT:USDT | +49.28% | $1,712,479.34 |
| ZCAT/USDT:USDT | +40.70% | $1,196,981.24 |
| VTHO/USDT:USDT | +23.60% | $2,633,149.91 |
| LONGXIA/USDT:USDT | +20.16% | $9,887,772.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIULAI/USDT:USDT | below_1h_threshold | +3.13% | +3.22% |
| VET/USDT:USDT | below_1h_threshold | +3.08% | +3.17% |
| POWR/USDT:USDT | below_1h_threshold | +2.87% | +2.97% |
| FLOCK/USDT:USDT | below_1h_threshold | +2.62% | +2.72% |
| BSV/USDT:USDT | below_1h_threshold | +1.61% | +1.71% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
