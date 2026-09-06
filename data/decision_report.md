# Decision Report

- generated_at: 2026-09-06T09:11:13.017353+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13807**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.36% / filled 20/20。**
- 全期間 MARKET基準: n=13807, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.36% | **+0.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| MARKET | 20/20 | 100.0% | +0.36% | **+0.36%** |
| LIMIT_BB3S | 4/15 | 26.7% | +0.69% | **+0.18%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.20% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +5.23% | **+3.14%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.57% | **+1.25%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.39% | **+1.04%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.15% | **+0.75%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.31% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$847.74** / 初期 $100.00 (+747.74%)
- 確定: 5113件 (Win 1535 / Loss 1672 / Flat 1906) / skip 5255件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OP/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $847.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$193.92** / 初期 $100.00 (+93.92%)
- 確定: 2552件 (Win 715 / Loss 606 / Flat 1231) / skip 4666件
- 成長率目線: 平均log +0.000260 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0046 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: OP/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.01% 残高後 $193.92

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.90** / 初期 $100.00 (+19.90%)
- 確定: 2419件 (Win 721 / Loss 920 / Flat 778) / pending 4件 / skip 2855件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000210 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: OP/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $119.90

## 6. Latest Market Context

- 更新: 2026-09-06T09:11:03.187925+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=79870.2
- Funnel: target 1054 → liquid 125 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARB/USDT:USDT | +48.43% | $156,458,988.05 |
| FLOCK/USDT:USDT | +40.17% | $1,527,150.39 |
| RAY/USDT:USDT | +33.78% | $3,372,660.97 |
| UAI/USDT:USDT | +22.50% | $13,156,276.53 |
| GRT/USDT:USDT | +16.85% | $1,738,417.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAY/USDT:USDT | below_1h_threshold | +1.91% | +1.83% |
| NEAR/USDT:USDT | below_1h_threshold | +1.64% | +1.56% |
| TIA/USDT:USDT | below_1h_threshold | +0.86% | +0.78% |
| ATOM/USDT:USDT | below_1h_threshold | +0.69% | +0.61% |
| MONAD/USDT:USDT | below_1h_threshold | +0.69% | +0.61% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
